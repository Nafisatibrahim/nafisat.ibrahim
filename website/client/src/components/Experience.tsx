import { motion } from "framer-motion";
import { Briefcase, Calendar, MapPin, GraduationCap } from "lucide-react";

export default function Experience() {
  const experiences = [
    {
      title: "Data Analyst",
      company: "Exyte",
      location: "Dallas, TX",
      period: "May 2024 – Aug 2025",
      tech: ["Python", "Power BI", "Excel", "Databricks", "Azure"],
      achievements: [
        "Analyzed construction project data to detect trends and risks, helping teams mitigate overruns.",
        "Automated forecasting workflows using Python & VBA, improving accuracy by 30%.",
        "Built real-time Power BI dashboards, reducing information search time by 50%.",
        "Prototyped clash-detection analytics in 3D models using Azure ML."
      ]
    },
    {
      title: "Business Analyst Extern",
      company: "HP",
      location: "Denton, TX",
      period: "Jan 2024 – May 2024",
      tech: ["SQL", "Excel", "Tableau"],
      achievements: [
        "Analyzed early-stage startup data using SQL and Excel for investment insights.",
        "Created Tableau dashboards to evaluate startup performance and market trends."
      ]
    }
  ];

  const education = [
    {
      school: "University of Waterloo",
      degree: "Master of Mathematics in Data Science",
      location: "Waterloo, ON",
      period: "May 2027 (Expected)",
      details: "Courses: Statistical Inference & Probability, Machine Learning"
    },
    {
      school: "University of North Texas",
      degree: "Bachelor of Science in Mathematics",
      location: "Denton, TX",
      period: "May 2024",
      details: ""
    }
  ];

  return (
    <section id="experience" className="py-20">
      <div className="container mx-auto px-4 md:px-6">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-16"
        >
          <h2 className="text-3xl font-bold mb-4 flex items-center gap-3">
            <span className="text-primary font-mono">03.</span> Experience & Education
          </h2>
          <div className="h-1 w-20 bg-primary rounded-full" />
        </motion.div>

        <div className="max-w-4xl mx-auto grid md:grid-cols-1 gap-16">
          {/* Work Experience */}
          <div>
            <h3 className="text-xl font-mono text-primary mb-8 flex items-center">
              <Briefcase className="w-5 h-5 mr-2" /> Work History
            </h3>
            <div className="relative border-l border-border ml-3 md:ml-6 space-y-12">
              {experiences.map((exp, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, x: -20 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  viewport={{ once: true }}
                  transition={{ delay: index * 0.2 }}
                  className="relative pl-8 md:pl-12"
                >
                  {/* Timeline Dot */}
                  <div className="absolute -left-[5px] top-2 w-3 h-3 bg-primary rounded-full ring-4 ring-background" />

                  <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-2">
                    <h4 className="text-2xl font-bold text-foreground">{exp.title}</h4>
                    <div className="flex items-center text-muted-foreground text-sm font-mono mt-1 sm:mt-0">
                      <Calendar className="w-4 h-4 mr-2" />
                      {exp.period}
                    </div>
                  </div>

                  <div className="flex items-center text-lg text-secondary mb-4 font-medium">
                    {exp.company}
                    <span className="mx-2">•</span>
                    <span className="text-sm text-muted-foreground flex items-center">
                      <MapPin className="w-4 h-4 mr-1" />
                      {exp.location}
                    </span>
                  </div>

                  <ul className="space-y-2 mb-4">
                    {exp.achievements.map((item, i) => (
                      <li key={i} className="text-muted-foreground leading-relaxed flex items-start">
                        <span className="mr-2 text-primary mt-1">▹</span>
                        {item}
                      </li>
                    ))}
                  </ul>

                  <div className="flex flex-wrap gap-2 mt-4">
                    {exp.tech.map((t) => (
                      <span key={t} className="text-xs font-mono px-2 py-1 bg-muted rounded border border-border">
                        {t}
                      </span>
                    ))}
                  </div>
                </motion.div>
              ))}
            </div>
          </div>

          {/* Education */}
          <div>
            <h3 className="text-xl font-mono text-primary mb-8 flex items-center">
              <GraduationCap className="w-5 h-5 mr-2" /> Education
            </h3>
            <div className="grid gap-6">
              {education.map((edu, index) => (
                 <motion.div
                    key={index}
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ delay: index * 0.2 }}
                    className="bg-card border border-border/50 p-6 rounded-lg hover:border-primary/30 transition-colors"
                 >
                    <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-2">
                        <h4 className="text-lg font-bold text-foreground">{edu.school}</h4>
                        <span className="text-sm font-mono text-primary">{edu.period}</span>
                    </div>
                    <p className="text-secondary font-medium mb-2">{edu.degree}</p>
                    <p className="text-sm text-muted-foreground flex items-center mb-2">
                        <MapPin className="w-3 h-3 mr-1" /> {edu.location}
                    </p>
                    {edu.details && (
                        <p className="text-sm text-muted-foreground border-t border-border/30 pt-2 mt-2">
                            {edu.details}
                        </p>
                    )}
                 </motion.div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
