import { BrowserRouter, Route, Routes } from "react-router-dom";
import {
  Contents,
  CreateDone,
  CreateTheater,
  Landing,
  Login,
  Main,
  NotFound,
  RegisterDetail,
  RegisterDone,
  // RegisterId,
  RegisterName,
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
        <Route path="/register/name" element={<RegisterName />} />
        {/* <Route path="/register/id" element={<RegisterId />} /> */}
        <Route path="/register/detail" element={<RegisterDetail />} />
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
