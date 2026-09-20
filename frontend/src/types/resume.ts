export interface ResumeAnalysis {
  match_score: number;
  matched_skills: string[];
  missing_skills: string[];
  extra_skills: string[];
  experience_match: boolean | null;
  education_match: boolean | null;
  education_or_experience: boolean;
  recommendations: string[];
  summary: string | null;
  ai_status: "available" | "unavailable";
}
