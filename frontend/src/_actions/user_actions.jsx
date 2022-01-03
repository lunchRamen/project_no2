import axios from "axios";

export const LOGIN_USER = "LOGIN_USER";
export const REGISTER_USER = "REGISTER_USER";

export function registerUser(dataToSubmit) {
  const request = axios.post("/register", dataToSubmit).then((response) => response.data);
  return {
    type: REGISTER_USER,
    payload: request,
  };
}

export function loginUser(dataToSubmit) {
  const request = axios.post("/login", dataToSubmit).then((response) => response.data);
  return {
    type: LOGIN_USER,
    payload: request,
  };
}
