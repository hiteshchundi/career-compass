function App() {
  return (
    <main className="min-h-screen bg-slate-100">
      <div className="mx-auto max-w-6xl px-6 py-10">

        <div className="mb-10 text-center">

          <h1 className="text-5xl font-bold text-slate-900">
            Career Compass
          </h1>

          <p className="mt-4 text-lg text-slate-600">
            AI-powered Resume Analysis
          </p>

        </div>

        <div className="rounded-2xl bg-white p-10 shadow-lg">

          <div className="border-2 border-dashed border-slate-300 rounded-xl p-16 text-center">

            <h2 className="text-2xl font-semibold">
              Upload your Resume
            </h2>

            <p className="mt-2 text-slate-500">
              PDF and DOCX supported
            </p>

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
            >
              Choose Resume
            </button>

          </div>

        </div>

      </div>
    </main>
  );
}

export default App;