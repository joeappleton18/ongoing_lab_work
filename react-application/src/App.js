import { Route, Routes } from 'react-router-dom';
import MainLayout from './components/MainLayout';
import Board from './pages/Board';
import Home from './pages/Home';
import NotFound from './pages/NotFound';
function App() {
  return (
    <Routes>
      <Route path="/" element={<MainLayout />}>
        <Route index element={<Home />} />
        <Route path="/board/:id" element={<Board />} />
        <Route path="*" element={<NotFound />} />
      </Route>
    </Routes>
  );
}


export default App;