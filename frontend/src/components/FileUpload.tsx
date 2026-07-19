import { useRef, useState } from "react";
import { analyzeResume } from "../api/resume";

interface FileUploadProps {
  onSuccess: (result: any) => void;
}

type StatusType = "success" | "error" | "info";

export default function FileUpload({ onSuccess }: FileUploadProps) {
  const inputRef = useRef<HTMLInputElement>(null);

  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const [jobDescription, setJobDescription] = useState("");

  const [loading, setLoading] = useState(false);

  const [status, setStatus] = useState("");

  const [statusType, setStatusType] = useState<StatusType>("info");

  async function handleUpload() {
    if (!selectedFile) return;

    if (!jobDescription.trim()) {
      setStatus("Please paste a Job Description.");
      setStatusType("error");
      return;
    }

    try {
      setLoading(true);

      setStatus("Analyzing...");
      setStatusType("info");

      const result = await analyzeResume(selectedFile, jobDescription);

      onSuccess(result);

      setStatus("Analysis Complete!");
      setStatusType("success");
    } catch (e) {
      console.error(e);

      setStatus("Analysis failed.");
      setStatusType("error");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="rounded-2xl bg-white p-10 shadow-lg">
      <h2 className="text-2xl font-semibold">Upload Resume</h2>

      <input
        ref={inputRef}
        hidden
        type="file"
        accept=".pdf,.docx"
        onChange={(e) => {
          if (e.target.files?.length) {
            setSelectedFile(e.target.files[0]);
          }
        }}
      />

      <button
        className="mt-6 rounded-xl bg-blue-600 px-6 py-3 text-white"
        onClick={() => inputRef.current?.click()}
      >
        Choose Resume
      </button>

      {selectedFile && <p className="mt-4">{selectedFile.name}</p>}

      <textarea
        className="mt-8 h-64 w-full rounded-lg border p-4"
        placeholder="Paste the Job Description here..."
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
      />

      <button
        disabled={!selectedFile || loading}
        className="mt-6 rounded-xl bg-green-600 px-8 py-3 text-white disabled:bg-gray-400"
        onClick={handleUpload}
      >
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>

      {status && (
        <div
          className={`mt-6 rounded-lg p-4 ${
            statusType === "success"
              ? "bg-green-100"
              : statusType === "error"
                ? "bg-red-100"
                : "bg-blue-100"
          }`}
        >
          {status}
        </div>
      )}
    </div>
  );
}
