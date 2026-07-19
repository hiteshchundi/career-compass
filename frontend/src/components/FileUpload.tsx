import { useState } from "react";
import { analyzeResume } from "../api/resume";
import type { ResumeAnalysis } from "../types/resume";

interface FileUploadProps {
  onSuccess: (result: ResumeAnalysis) => void;
}

export default function FileUpload({
  onSuccess,
}: FileUploadProps) {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleUpload() {
    if (!selectedFile) return;

    try {
      setLoading(true);

      const result = await analyzeResume(selectedFile);

      onSuccess(result);
    } catch (error) {
      console.error(error);
      alert("Failed to analyze resume.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="rounded-2xl bg-white p-10 shadow-lg">

      <h2 className="text-2xl font-semibold">
        Upload Resume
      </h2>

      <input
        className="mt-6 block"
        type="file"
        accept=".pdf,.docx"
        onChange={(event) => {
          if (event.target.files?.length) {
            setSelectedFile(event.target.files[0]);
          }
        }}
      />

      <button
        className="
          mt-6
          rounded-xl
          bg-blue-600
          px-8
          py-3
          text-white
          hover:bg-blue-700
          disabled:bg-gray-400
        "
        disabled={!selectedFile || loading}
        onClick={handleUpload}
      >
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>

    </div>
  );
}