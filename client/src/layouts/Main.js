import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Navbar } from 'react-bootstrap';
import { Outlet } from 'react-router-dom';

function Main({ children }) {
	return (
		<div>
			<Navbar bg="dark" variant="dark" expand="lg">
				<h3> Project Board Name</h3>
				<Navbar.Brand href="#">The Great Project</Navbar.Brand>
			</Navbar>
			<Container fluid className="mt-4">
				<Outlet />
			</Container>

		</div>
	);
}

export default Main;