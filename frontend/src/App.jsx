import { Routes, Route } from "react-router-dom";
import { Home } from "./pages/Home";
import { Login } from "./components/Login";
import { Register } from "./components/Register";
import { Protected } from "./components/Protected";
function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Login />}></Route>
        <Route
          path="home"
          element={
            <Protected>
              <Home />
            </Protected>
          }
        ></Route>
        <Route path="register" element={<Register />}></Route>
      </Routes>
    </>
  );
}

export default App;
