import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Navbar } from 'react-bootstrap';
import { Link, Outlet } from 'react-router-dom';


function Main({ children }) {
	return (
		<div>
			<Navbar bg="dark" variant="dark" className='p-3'>
				<Link to="/">
					<Navbar.Brand href="#">The Great Project</Navbar.Brand>
				</Link>
			</Navbar>
			<Container fluid className="mt-4">
				<Outlet />
			</Container>

		</div>
	);
}

export default Main;