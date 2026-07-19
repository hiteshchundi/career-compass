import { useRef, useState } from "react";
import { analyzeResume, tailorResume } from "../api/resume";

interface FileUploadProps {
  onSuccess: (result: any) => void;
}

type StatusType = "success" | "error" | "info";

export default function FileUpload({ onSuccess }: FileUploadProps) {
  const inputRef = useRef<HTMLInputElement>(null);

  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const [jobDescription, setJobDescription] = useState("");

  const [loading, setLoading] = useState(false);

  const [tailoring, setTailoring] = useState(false);

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

  async function handleTailorResume() {
    if (!selectedFile) return;

    if (!jobDescription.trim()) {
      setStatus("Please paste a Job Description.");
      setStatusType("error");
      return;
    }

    try {
      setTailoring(true);

      setStatus("Generating tailored resume...");
      setStatusType("info");

      const blob = await tailorResume(selectedFile, jobDescription);

      const url = window.URL.createObjectURL(blob);

      const link = document.createElement("a");

      link.href = url;
      link.download = "tailored_resume.docx";

      document.body.appendChild(link);

      link.click();

      link.remove();

      window.URL.revokeObjectURL(url);

      setStatus("Tailored resume downloaded!");
      setStatusType("success");
    } catch (e) {
      console.error(e);

      setStatus("Failed to generate tailored resume.");
      setStatusType("error");
    } finally {
      setTailoring(false);
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

      <div className="mt-6 flex gap-4">
        <button
          disabled={!selectedFile || loading}
          className="rounded-xl bg-green-600 px-8 py-3 text-white disabled:bg-gray-400"
          onClick={handleUpload}
        >
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>

        <button
          disabled={!selectedFile || tailoring || loading}
          className="rounded-xl bg-purple-600 px-8 py-3 text-white disabled:bg-gray-400"
          onClick={handleTailorResume}
        >
          {tailoring ? "Generating..." : "Generate Tailored Resume"}
        </button>
      </div>

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
