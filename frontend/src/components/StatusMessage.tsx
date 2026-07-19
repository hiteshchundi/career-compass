interface StatusMessageProps {
  type: "success" | "error" | "info";
  message: string;
}

export default function StatusMessage({
  type,
  message,
}: StatusMessageProps) {
  if (!message) return null;

  const styles = {
    success: "bg-green-100 text-green-800 border border-green-300",
    error: "bg-red-100 text-red-800 border border-red-300",
    info: "bg-blue-100 text-blue-800 border border-blue-300",
  };

  return (
    <div className={`mt-6 rounded-xl p-4 ${styles[type]}`}>
      {message}
    </div>
  );
}