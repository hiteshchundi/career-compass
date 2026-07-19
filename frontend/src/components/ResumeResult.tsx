interface Props {
  result: any;
}

export default function ResumeResult({ result }: Props) {
  if (!result) return null;

  return (
    <div className="mt-10 rounded-2xl bg-white p-10 shadow-lg">
      <h2 className="text-2xl font-bold">ATS Match Score</h2>

      <div className="mt-4 text-6xl font-bold text-green-600">
        {result.match_score}%
      </div>

      <h3 className="mt-8 text-xl font-semibold">Matching Skills</h3>

      <ul className="mt-2 list-disc pl-6">
        {result.matching_skills?.map((skill: string) => (
          <li key={skill}>{skill}</li>
        ))}
      </ul>

      <h3 className="mt-8 text-xl font-semibold">Missing Skills</h3>

      <ul className="mt-2 list-disc pl-6">
        {result.missing_skills?.map((skill: string) => (
          <li key={skill}>{skill}</li>
        ))}
      </ul>

      <h3 className="mt-8 text-xl font-semibold">Recommendations</h3>

      <ul className="mt-2 list-disc pl-6">
        {result.recommendations?.map((item: string) => (
          <li key={item}>{item}</li>
        ))}
      </ul>

      <div className="mt-8">
        <p>
          <strong>Experience Match:</strong>{" "}
          {result.experience_match ? "✅ Yes" : "❌ No"}
        </p>

        <p>
          <strong>Education Match:</strong>{" "}
          {result.education_match ? "✅ Yes" : "❌ No"}
        </p>
      </div>
    </div>
  );
}
