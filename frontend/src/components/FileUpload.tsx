import { useRef, useState } from "react";
import { analyzeResume } from "../api/resume";
import type { ResumeAnalysis } from "../types/resume";

interface FileUploadProps {
  onSuccess: (result: ResumeAnalysis | null) => void;
}

type StatusType = "success" | "error" | "info";

export default function FileUpload({
  onSuccess,
}: FileUploadProps) {
  const inputRef = useRef<HTMLInputElement>(null);

  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);

  const [status, setStatus] = useState("");
  const [statusType, setStatusType] =
    useState<StatusType>("info");

  async function handleUpload() {
    if (!selectedFile) return;

    try {
      setLoading(true);

      setStatus("Analyzing your resume...");
      setStatusType("info");

      const result = await analyzeResume(selectedFile);

      onSuccess(result);

      setStatus("Resume analyzed successfully!");
      setStatusType("success");
    } catch (error) {
      console.error(error);

      setStatus(
        "Failed to analyze the resume. Please upload a valid PDF or DOCX file."
      );

      setStatusType("error");
    } finally {
      setLoading(false);
    }
  }

  function reset() {
    setSelectedFile(null);

    onSuccess(null);

    setStatus("");
    setStatusType("info");

    if (inputRef.current) {
      inputRef.current.value = "";
    }
  }

  return (
    <div className="rounded-2xl bg-white p-10 shadow-lg">

      <h2 className="text-2xl font-semibold">
        Upload Resume
      </h2>

      <p className="mt-2 text-slate-500">
        Upload your resume in PDF or DOCX format
      </p>

      <input
        ref={inputRef}
        hidden
        type="file"
        accept=".pdf,.docx"
        onChange={(event) => {
          if (event.target.files?.length) {
            setSelectedFile(event.target.files[0]);

            setStatus("");
            setStatusType("info");
          }
        }}
      />

      <button
        className="
          mt-8
          rounded-xl
          bg-blue-600
          px-8
          py-3
          text-white
          transition
          hover:bg-blue-700
        "
        onClick={() => inputRef.current?.click()}
      >
        Choose Resume
      </button>

      {selectedFile && (
        <div className="mt-6 rounded-lg bg-slate-100 p-4">

          <p className="font-semibold text-slate-700">
            Selected File
          </p>

          <p className="mt-1 text-slate-600">
            {selectedFile.name}
          </p>

        </div>
      )}

      <div className="mt-8 flex gap-4">

        <button
          disabled={!selectedFile || loading}
          className="
            rounded-xl
            bg-green-600
            px-8
            py-3
            text-white
            transition
            hover:bg-green-700
            disabled:cursor-not-allowed
            disabled:bg-gray-400
          "
          onClick={handleUpload}
        >
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>

        <button
          className="
            rounded-xl
            bg-gray-600
            px-8
            py-3
            text-white
            transition
            hover:bg-gray-700
          "
          onClick={reset}
        >
          Upload Another Resume
        </button>

      </div>

      {status && (
        <div
          className={`mt-6 rounded-lg p-4 ${
            statusType === "success"
              ? "bg-green-100 text-green-800"
              : statusType === "error"
              ? "bg-red-100 text-red-800"
              : "bg-blue-100 text-blue-800"
          }`}
        >
          {status}
        </div>
      )}

    </div>
  );
}