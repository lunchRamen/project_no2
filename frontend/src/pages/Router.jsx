import { BrowserRouter, Route, Routes } from "react-router-dom";
import {
  Contents,
  CreateDone,
  CreateTheater,
  Landing,
  Login,
  Main,
  NotFound,
  RegisterStep2,
  RegisterDone,
  RegisterStep1,
  TheaterList,
  Theater,
} from ".";
import { Header } from "../components";

const Router = () => {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/register/step1" element={<RegisterStep1 />} />
        <Route path="/register/step2" element={<RegisterStep2 />} />
        <Route path="/register/done" element={<RegisterDone />} />
        <Route path="/login" element={<Login />} />
        <Route path="/main" element={<Main />} />
        <Route path="/contents" element={<Contents />} />
        <Route path="/theater_list" element={<TheaterList />} />
        <Route path="/theater/:id" element={<Theater />} />
        <Route path="/create_theater" element={<CreateTheater />} />
        <Route path="/create_done" element={<CreateDone />} />
        <Route path="/*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
};

export default Router;
