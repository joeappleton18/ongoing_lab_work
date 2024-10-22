import 'bootstrap/dist/css/bootstrap.min.css';
import { Route, Routes } from 'react-router-dom';
import MainLayout from './layouts/Main';
import BoardPage from './pages/Board';
import ProjectPage from './pages/Project';
function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<MainLayout />}>
          <Route index element={<ProjectPage />} />
          <Route path="board/:id" element={<BoardPage />} />
        </Route>

      </Routes>
    </div>
  );
}

export default App;
