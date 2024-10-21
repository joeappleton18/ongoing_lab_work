import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState } from 'react';
import { Button, Card, Col, Container, Form, Navbar, Row } from 'react-bootstrap';
import { DndProvider, useDrag, useDrop } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';

const ItemType = {
  CARD: 'card'
};

const initialData = {
  boards: [
    {
      id: '1',
      name: 'To Do',
      cards: [
        { id: '1', text: 'Task 1' },
        { id: '2', text: 'Task 2' }
      ]
    },
    {
      id: '2',
      name: 'In Progress',
      cards: [
        { id: '3', text: 'Task 3' },
        { id: '4', text: 'Task 4' }
      ]
    },
    {
      id: '3',
      name: 'Done',
      cards: [
        { id: '5', text: 'Task 5' }
      ]
    }
  ]
};

function App() {
  const [data, setData] = useState(initialData);

  const addCard = (boardId, cardText) => {
    const newCard = { id: Date.now().toString(), text: cardText };
    const updatedBoards = data.boards.map(board => {
      if (board.id === boardId) {
        return { ...board, cards: [...board.cards, newCard] };
      }
      return board;
    });
    setData({ ...data, boards: updatedBoards });
  };

  // Handle card move between boards and within the same board
  const moveCard = (draggedCard, sourceBoardId, targetBoardId, sourceIndex, targetIndex) => {
    const sourceBoard = data.boards.find(board => board.id === sourceBoardId);
    const targetBoard = data.boards.find(board => board.id === targetBoardId);

    const updatedSourceCards = Array.from(sourceBoard.cards);
    const [removedCard] = updatedSourceCards.splice(sourceIndex, 1);

    if (sourceBoardId === targetBoardId) {
      // Reordering within the same board (vertical drag)
      updatedSourceCards.splice(targetIndex, 0, removedCard);
      const updatedBoards = data.boards.map(board => {
        if (board.id === sourceBoardId) {
          return { ...board, cards: updatedSourceCards };
        }
        return board;
      });
      setData({ ...data, boards: updatedBoards });
    } else {
      // Moving card between different boards (horizontal drag)
      const updatedTargetCards = Array.from(targetBoard.cards);
      updatedTargetCards.splice(targetIndex, 0, removedCard);

      const updatedBoards = data.boards.map(board => {
        if (board.id === sourceBoardId) {
          return { ...board, cards: updatedSourceCards };
        }
        if (board.id === targetBoardId) {
          return { ...board, cards: updatedTargetCards };
        }
        return board;
      });
      setData({ ...data, boards: updatedBoards });
    }
  };

  return (
    <>
      {/* Navbar/Header */}
      <Navbar bg="dark" variant="dark" expand="lg">
        <h3> Project Board Name</h3>
        <Navbar.Brand href="#">Trello Clone</Navbar.Brand>
      </Navbar>

      {/* DndProvider wraps the app where drag-and-drop is used */}
      <DndProvider backend={HTML5Backend}>
        <Container fluid className="mt-4">
          <Row>
            {data.boards.map((board, boardIndex) => (
              <Col key={board.id} md={4}>
                <Board
                  board={board}
                  boardIndex={boardIndex}
                  addCard={addCard}
                  moveCard={moveCard}
                />
              </Col>
            ))}
          </Row>
        </Container>
      </DndProvider>
    </>
  );
}

function Board({ board, addCard, moveCard }) {
  const [newCardText, setNewCardText] = useState('');

  const handleAddCard = () => {
    if (newCardText.trim() !== '') {
      addCard(board.id, newCardText);
      setNewCardText('');
    }
  };

  const [, drop] = useDrop({
    accept: ItemType.CARD,
    hover: () => { },
  });

  return (
    <Card className="mb-4">
      <Card.Header className="bg-primary text-white">
        <h5>{board.name}</h5>
      </Card.Header>
      <Card.Body ref={drop}>
        {board.cards.map((card, index) => (
          <CardComponent
            key={card.id}
            card={card}
            index={index}
            boardId={board.id}
            moveCard={moveCard}
          />
        ))}
        <Form.Control
          type="text"
          value={newCardText}
          placeholder="Add a new task..."
          onChange={e => setNewCardText(e.target.value)}
        />
        <Button variant="primary" className="mt-2" onClick={handleAddCard}>
          Add Task
        </Button>
      </Card.Body>
    </Card>
  );
}

function CardComponent({ card, index, boardId, moveCard }) {
  const [, drag] = useDrag({
    type: ItemType.CARD,
    item: { card, index, boardId },
  });

  const [, drop] = useDrop({
    accept: ItemType.CARD,
    hover(draggedItem) {
      if (draggedItem.index === index && draggedItem.boardId === boardId) return;

      // If dragging within the same board, reorder the cards
      moveCard(draggedItem.card, draggedItem.boardId, boardId, draggedItem.index, index);
      draggedItem.index = index;
      draggedItem.boardId = boardId;
    }
  });

  return (
    <div ref={node => drag(drop(node))} style={{ marginBottom: '10px' }}>
      <Card>
        <Card.Body>{card.text}</Card.Body>
      </Card>
    </div>
  );
}

export default App;
