import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://127.0.0.1:8000",
});
console.log("VITE_API_URL =", import.meta.env.VITE_API_URL);
export async function analyzeResume(file: File, jobDescription: string) {
  const formData = new FormData();

  formData.append("resume", file);
  formData.append("job_description", jobDescription);

  const response = await api.post("/analyze", formData);
  return response.data;
}

export async function tailorResume(file: File, jobDescription: string) {
  const formData = new FormData();

  formData.append("resume", file);
  formData.append("job_description", jobDescription);

  const response = await api.post("/tailor", formData, {
    responseType: "blob",
  });
  return response.data;
}
