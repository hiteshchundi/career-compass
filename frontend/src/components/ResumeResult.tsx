interface Props {
  result: any;
}

export default function ResumeResult({ result }: Props) {
  if (!result) return null;

  const score = result.match_score ?? 0;

  let scoreLabel = "Weak Match";
  let scoreColor = "text-red-600";

  if (score >= 80) {
    scoreLabel = "Strong Match";
    scoreColor = "text-green-600";
  } else if (score >= 60) {
    scoreLabel = "Moderate Match";
    scoreColor = "text-yellow-600";
  }

  return (
    <div className="mt-10 rounded-2xl bg-white p-10 shadow-lg">
      {/* Score */}

      <h2 className="text-2xl font-bold">ATS Match Score</h2>

      <div className={`mt-4 text-6xl font-bold ${scoreColor}`}>{score}%</div>

      <p className={`mt-2 text-xl font-semibold ${scoreColor}`}>{scoreLabel}</p>

      {/* AI Summary */}

      {result.summary && (
        <>
          <h3 className="mt-10 text-xl font-semibold">
            🤖 AI Recruiter Summary
          </h3>

          <div className="mt-3 rounded-lg border border-gray-200 bg-gray-50 p-5 leading-7 text-gray-700">
            {result.summary}
          </div>
        </>
      )}

      {/* Matching Skills */}

      <h3 className="mt-10 text-xl font-semibold">Matching Skills</h3>

      {result.matched_skills?.length ? (
        <ul className="mt-2 list-disc pl-6">
          {result.matched_skills.map((skill: string) => (
            <li key={skill}>{skill}</li>
          ))}
        </ul>
      ) : (
        <p className="mt-2 text-gray-500">No matching skills identified.</p>
      )}

      {/* Missing Skills */}

      <h3 className="mt-8 text-xl font-semibold">Missing Skills</h3>

      {result.missing_skills?.length ? (
        <ul className="mt-2 list-disc pl-6">
          {result.missing_skills.map((skill: string) => (
            <li key={skill}>{skill}</li>
          ))}
        </ul>
      ) : (
        <p className="mt-2 text-green-600">No important skills are missing.</p>
      )}

      {/* Recommendations */}

      <h3 className="mt-8 text-xl font-semibold">Recommendations</h3>

      {result.recommendations?.length ? (
        <ul className="mt-2 list-disc pl-6">
          {result.recommendations.map((item: string) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      ) : (
        <p className="mt-2 text-green-600">No recommendations.</p>
      )}

      {/* Experience & Education */}

      <div className="mt-10 grid gap-4 md:grid-cols-2">
        <div className="rounded-lg border p-4">
          <h4 className="font-semibold">Experience Match</h4>

          <p className="mt-2 text-lg">
            {result.experience_match ? "✅ Yes" : "❌ No"}
          </p>
        </div>

        <div className="rounded-lg border p-4">
          <h4 className="font-semibold">Education Match</h4>

          <p className="mt-2 text-lg">
            {result.education_match ? "✅ Yes" : "❌ No"}
          </p>
        </div>
      </div>
    </div>
  );
}
