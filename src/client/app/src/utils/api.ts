import { initData } from "@tma.js/sdk";
import axios from "axios";

const BASE_URL = import.meta.env.VITE_VASE_API_URL

interface Response {
  data: any;
  message: string | null;
  success: boolean
}

const request = async (
  endpoint: string,
  method: "GET" | "POST" | "PUT" | "DELETE" = "GET",
  data?: any
) => {
  const response = await axios.request({
    url: `${BASE_URL}/api/v1/${endpoint}`,
    method: method,
    headers: {
      Authorization: `tma ${initData.raw()}`,
      Accept: "application/json",
      "Content-Type": "application/json"
    },
    data: data ? JSON.stringify(data) : undefined
  })

  return response.data as Response
}

export default request;