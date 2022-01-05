import axios from "axios";
export const LOGIN_USER = "LOGIN_USER";
export const REGISTER_USER = "REGISTER_USER";
export const LOGOUT_USER = "LOGOUT_USER";

export function registerUser(dataToSubmit) {
  const request = axios.post("/user/register", dataToSubmit).then((response) => response.data);
  return {
    type: REGISTER_USER,
    payload: request,
  };
}

export function loginUser(dataToSubmit) {
  const request = axios.post("/user/login", dataToSubmit).then((response) => response.data);
  return {
    type: LOGIN_USER,
    payload: request,
  };
}

export function logoutUser() {
  const request = axios.get("/user/logout").then((response) => response.data);
  return {
    type: LOGOUT_USER,
    payload: request,
  };
}
