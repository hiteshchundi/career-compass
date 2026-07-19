import { useState } from "react";
import FileUpload from "./components/FileUpload";
import ResumeResult from "./components/ResumeResult";
import type { ResumeAnalysis } from "./types/resume";

function App() {
  const [analysis, setAnalysis] =
    useState<ResumeAnalysis | null>(null);

  return (
    <main className="min-h-screen bg-slate-100">

      <div className="mx-auto max-w-6xl px-6 py-10">

        <div className="mb-10 text-center">

          <h1 className="text-5xl font-bold">
            Career Compass
          </h1>

          <p className="mt-4 text-slate-600">
            AI-powered Resume Analysis
          </p>

        </div>

        <FileUpload onSuccess={setAnalysis} />

        <ResumeResult result={analysis} />

      </div>

    </main>
  );
}

export default App;