import { Card, Col, Container, Row } from 'react-bootstrap';

const initialData = {
	lists: [
		{
			id: '0',
			name: 'Backlog',
			tasks: [
				{ id: '1', text: 'Task 1' },
				{ id: '2', text: 'Task 2' }
			]
		},
		{
			id: '1',
			name: 'To Do',
			tasks: [
				{ id: '1', text: 'Task 1' },
				{ id: '2', text: 'Task 2' }
			]
		},
		{
			id: '2',
			name: 'In Progress',
			tasks: [
				{ id: '3', text: 'Task 3' },
				{ id: '4', text: 'Task 4' }
			]
		},
		{
			id: '3',
			name: 'Done',
			tasks: [
				{ id: '5', text: 'Task 5' }
			]
		}
	]
};


function Board() {
	return (
		<Container fluid>
			<Row>
				{initialData.lists.map((list) => (
					<Col key={list.id} xs={12} md={3} className="mb-4">
						<Card>
							<Card.Header>{list.name}</Card.Header>
							<Card.Body>
								{list.tasks.map((task) => (
									<Card key={task.id} className="mb-2">
										<Card.Body>{task.text}</Card.Body>
									</Card>
								))}
							</Card.Body>
						</Card>
					</Col>
				))}
			</Row>
		</Container>
	)
}

export default Board;