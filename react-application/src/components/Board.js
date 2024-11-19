import { useState } from 'react';
import Card from 'react-bootstrap/Card';
import img from '../assets/cover.jpg';
function Board({ title }) {

	const [bg, setBg] = useState("success");
	const [txt, setTxt] = useState("white");


	const handleMouseEnter = () => {
		setBg("danger");
		setTxt("primary");
	};

	const handleMouseLeave = () => {
		setBg("success");
		setTxt("white");
	};

	return (
		<Card bg={bg} text={txt} onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave} style={{ cursor: "pointer" }} className="mb-2 mt-2">
			<Card.Img variant="top" src={img} />
			<Card.Body>
				<Card.Title>{title}</Card.Title>
			</Card.Body>
		</Card>
	);
}

export default Board;