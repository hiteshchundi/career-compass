interface Props {
  skills: string[];
}

export default function SkillsCard({
  skills,
}: Props) {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-lg">

      <h2 className="mb-6 text-xl font-bold">
        🛠 Skills
      </h2>

      {skills.length === 0 ? (
        <p className="text-slate-500">
          No skills detected.
        </p>
      ) : (
        <div className="flex flex-wrap gap-3">
          {skills.map((skill) => (
            <span
              key={skill}
              className="
                rounded-full
                bg-blue-100
                px-4
                py-2
                text-sm
                font-medium
                text-blue-800
              "
            >
              {skill}
            </span>
          ))}
        </div>
      )}

    </div>
  );
}