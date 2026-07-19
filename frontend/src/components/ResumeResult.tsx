import type { ResumeAnalysis } from "../types/resume";

interface Props {
  result: ResumeAnalysis | null;
}

export default function ResumeResult({
  result,
}: Props) {
  if (!result) return null;

  return (
    <div className="mt-10 rounded-2xl bg-white p-10 shadow-lg">

      <h2 className="mb-6 text-2xl font-bold">
        Resume Analysis
      </h2>

      <div className="space-y-2">

        <p>
          <strong>Email:</strong>{" "}
          {result.contact.email ?? "-"}
        </p>

        <p>
          <strong>Phone:</strong>{" "}
          {result.contact.phone ?? "-"}
        </p>

        <p>
          <strong>LinkedIn:</strong>{" "}
          {result.contact.linkedin ?? "-"}
        </p>

        <p>
          <strong>GitHub:</strong>{" "}
          {result.contact.github ?? "-"}
        </p>

      </div>

      <h3 className="mt-8 text-xl font-semibold">
        Skills
      </h3>

      <div className="mt-4 flex flex-wrap gap-2">

        {result.skills.map((skill) => (
          <span
            key={skill}
            className="rounded-full bg-blue-100 px-4 py-2"
          >
            {skill}
          </span>
        ))}

      </div>

    </div>
  );
}