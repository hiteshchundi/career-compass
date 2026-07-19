import {
  Mail,
  Phone,
  Globe,
  User,
} from "lucide-react";

interface Props {
  contact: {
    email?: string;
    phone?: string;
    linkedin?: string;
    github?: string;
  };
}

export default function ContactCard({
  contact,
}: Props) {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-lg">

      <h2 className="mb-6 text-xl font-bold">
        👤 Contact Information
      </h2>

      <div className="space-y-5">

        <div className="flex items-center gap-3">
          <Mail size={20} />
          <span>{contact.email || "-"}</span>
        </div>

        <div className="flex items-center gap-3">
          <Phone size={20} />
          <span>{contact.phone || "-"}</span>
        </div>

        <div className="flex items-center gap-3">
          <Globe size={20} />
          <span>{contact.linkedin || "-"}</span>
        </div>

        <div className="flex items-center gap-3">
          <User size={20} />
          <span>{contact.github || "-"}</span>
        </div>

      </div>

    </div>
  );
}