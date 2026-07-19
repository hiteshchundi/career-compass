export default function LoadingSpinner() {
  return (
    <div className="flex items-center gap-3">
      <div className="h-5 w-5 animate-spin rounded-full border-4 border-blue-600 border-t-transparent" />
      <span className="text-sm font-medium text-slate-700">
        Analyzing your resume...
      </span>
    </div>
  );
}