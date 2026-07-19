export interface ResumeAnalysis {
  contact: {
    name?: string;
    email?: string;
    phone?: string;
    location?: string;
    linkedin?: string;
    github?: string;
  };

  skills: string[];

  education: unknown[];

  experience: unknown[];

  projects: unknown[];

  certifications: unknown[];
}