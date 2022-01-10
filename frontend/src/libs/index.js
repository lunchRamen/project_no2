import axios from "axios";

const baseUrl = process.env.REACT_APP_BASE_URL;

export const client = axios.create({ 
  baseURL: `${baseUrl}/api`,
  headers: {
    "Content-Type": "application/json",
  },
});