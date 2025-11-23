import { motion } from "framer-motion";
import { Code2, Database, BarChart3, Terminal, LayoutTemplate, Cloud } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";

export default function Skills() {
  const skillCategories = [
    {
      title: "Programming & Scripting",
      icon: <Code2 className="w-8 h-8 text-primary" />,
      skills: ["Python", "SQL", "VBA (Excel)", "Bash/Shell"],
    },
    {
      title: "Data Analysis & Viz",
      icon: <BarChart3 className="w-8 h-8 text-primary" />,
      skills: ["Power BI", "Tableau", "Excel", "Matplotlib", "Seaborn"],
    },
    {
      title: "Machine Learning",
      icon: <Terminal className="w-8 h-8 text-primary" />,
      skills: ["TensorFlow", "Scikit-learn", "Pandas", "NumPy", "CNNs"],
    },
    {
      title: "Cloud & DevOps",
      icon: <Cloud className="w-8 h-8 text-primary" />,
      skills: ["Azure", "Databricks", "GCP", "Git", "GitHub", "Heroku"],
    },
    {
      title: "Web Frameworks",
      icon: <LayoutTemplate className="w-8 h-8 text-primary" />,
      skills: ["Streamlit", "Flask", "HTML/CSS"],
    },
  ];

  return (
    <section id="skills" className="py-20 bg-muted/30">
      <div className="container mx-auto px-4 md:px-6">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-12"
        >
          <h2 className="text-3xl font-bold mb-4 flex items-center gap-3">
            <span className="text-primary font-mono">02.</span> Technical Skills
          </h2>
          <div className="h-1 w-20 bg-primary rounded-full" />
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {skillCategories.map((category, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.1 }}
            >
              <Card className="bg-card border-border/50 hover:border-primary/50 transition-colors h-full">
                <CardContent className="p-6">
                  <div className="mb-4 bg-primary/10 w-fit p-3 rounded-lg">
                    {category.icon}
                  </div>
                  <h3 className="text-xl font-semibold mb-4">{category.title}</h3>
                  <div className="flex flex-wrap gap-2">
                    {category.skills.map((skill) => (
                      <span
                        key={skill}
                        className="px-3 py-1 bg-secondary/10 text-secondary text-sm rounded-full font-mono"
                      >
                        {skill}
                      </span>
                    ))}
                  </div>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
