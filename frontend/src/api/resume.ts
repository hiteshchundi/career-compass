import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export async function analyzeResume(file: File, jobDescription: string) {
  const formData = new FormData();

  formData.append("resume", file);
  formData.append("job_description", jobDescription);

  const response = await api.post("/analyze", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
}
