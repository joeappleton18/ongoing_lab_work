import { Col, Container, Row } from "react-bootstrap";
import { Link } from "react-router-dom";
import Board from "../components/Board";
function Home() {
	return (
		<Container>
			<Row>

				<Col xs={12} md={4}><Link to="/board/1" style={{ textDecoration: "none" }}><Board title="Migration from legacy PHP code to JavaScript" /></Link></Col>
				<Col xs={12} md={4}><Link to="/board/1" style={{ textDecoration: "none" }}><Board title="Create designs for user interface" /></Link></Col>
				<Col xs={12} md={4}><Link to="/board/1" style={{ textDecoration: "none" }}><Board title={"Influencer marketing" + "campaign"} /></Link></Col>
			</Row>
		</Container>
	);
}


export default Home;