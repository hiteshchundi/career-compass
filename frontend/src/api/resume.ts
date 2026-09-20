import axios from "axios";
import type { ResumeAnalysis } from "../types/resume";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://127.0.0.1:8000",
});

async function errorMessage(error: unknown, fallback: string): Promise<string> {
  if (!axios.isAxiosError(error)) return fallback;
  const data = error.response?.data;
  if (data instanceof Blob) {
    try {
      const parsed = JSON.parse(await data.text());
      return typeof parsed.detail === "string" ? parsed.detail : fallback;
    } catch { return fallback; }
  }
  return typeof data?.detail === "string" ? data.detail : fallback;
}

export async function analyzeResume(file: File, jobDescription: string): Promise<ResumeAnalysis> {
  const formData = new FormData();

  formData.append("resume", file);
  formData.append("job_description", jobDescription);

  try {
    const response = await api.post<ResumeAnalysis>("/analyze", formData);
    return response.data;
  } catch (error) {
    throw new Error(await errorMessage(error, "Analysis failed. Please try again."));
  }
}

export async function tailorResume(file: File, jobDescription: string) {
  const formData = new FormData();

  formData.append("resume", file);
  formData.append("job_description", jobDescription);

  try {
    const response = await api.post<Blob>("/tailor", formData, { responseType: "blob" });
    return response.data;
  } catch (error) {
    throw new Error(await errorMessage(error, "Resume generation failed. Please try again."));
  }
}
