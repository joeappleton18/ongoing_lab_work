import { Card, Col, Container, Row } from 'react-bootstrap';

function Board() {
	return (
		<Container fluid>
			<Row>
				<Col xs={12} md={3} className="mb-4">
					<Card>
						<Card.Header>Backlog</Card.Header>
						<Card.Body>
							<Card className="mb-2">
								<Card.Body>Task 1</Card.Body>
							</Card>
							<Card className="mb-2">
								<Card.Body>Task 2</Card.Body>
							</Card>
						</Card.Body>
					</Card>
				</Col>

				<Col xs={12} md={3} className="mb-4">
					<Card>
						<Card.Header>To Do</Card.Header>
						<Card.Body>
							<Card className="mb-2">
								<Card.Body>Task 1</Card.Body>
							</Card>
							<Card className="mb-2">
								<Card.Body>Task 2</Card.Body>
							</Card>
						</Card.Body>
					</Card>
				</Col>

				<Col xs={12} md={3} className="mb-4">
					<Card>
						<Card.Header>In Progress</Card.Header>
						<Card.Body>
							<Card className="mb-2">
								<Card.Body>Task 3</Card.Body>
							</Card>
							<Card className="mb-2">
								<Card.Body>Task 4</Card.Body>
							</Card>
						</Card.Body>
					</Card>
				</Col>

				<Col xs={12} md={3} className="mb-4">
					<Card>
						<Card.Header>Done</Card.Header>
						<Card.Body>
							<Card className="mb-2">
								<Card.Body>Task 5</Card.Body>
							</Card>
						</Card.Body>
					</Card>
				</Col>
			</Row>
		</Container>
	);
}

export default Board;