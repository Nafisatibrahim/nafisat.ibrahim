import { motion } from "framer-motion";
import { Github, ExternalLink, FolderGit2 } from "lucide-react";
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";

export default function Projects() {
  const projects = [
    {
      title: "DietVision.ai",
      category: "Applied AI + Gen AI",
      period: "Sep 2025 – Nov 2025",
      description: "AI-powered nutrition assistant that analyzes meal images and recommends healthier alternatives using a CNN-based food classification model. Integrated Gemini chatbot for dietary guidance.",
      tech: ["Python", "TensorFlow", "Streamlit", "Google Cloud", "Gemini API"],
      links: {
        github: "https://github.com/Nafisatibrahim/DietVision-TheSmartPlaters",
        demo: "#" // No demo link provided in resume, using placeholder
      }
    },
    {
      title: "Facial Emotion Detection",
      category: "Computer Vision (CNN)",
      period: "Jan 2025 – May 2025",
      description: "Developed a Convolutional Neural Network (CNN) to classify facial emotions from image input. Deployed as a real-time web app using Streamlit.",
      tech: ["Python", "TensorFlow", "Streamlit", "OpenCV"],
      links: {
        github: "https://github.com/Nafisatibrahim", // Using general github as placeholder
        demo: "https://nafisat-ibrahim-facial-emotion-detection.streamlit.app/"
      }
    }
  ];

  return (
    <section id="projects" className="py-20 bg-muted/30">
      <div className="container mx-auto px-4 md:px-6">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-12"
        >
          <h2 className="text-3xl font-bold mb-4 flex items-center gap-3">
            <span className="text-primary font-mono">04.</span> Featured Projects
          </h2>
          <div className="h-1 w-20 bg-primary rounded-full" />
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {projects.map((project, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.1 }}
            >
              <Card className="h-full flex flex-col bg-card border-border/50 hover:border-primary/50 transition-all hover:shadow-lg hover:shadow-primary/10 group">
                <CardHeader>
                  <div className="flex justify-between items-start mb-2">
                    <FolderGit2 className="w-10 h-10 text-primary mb-2" />
                    <div className="flex gap-2">
                      {project.links.github && (
                        <a href={project.links.github} target="_blank" rel="noreferrer" className="text-muted-foreground hover:text-primary transition-colors">
                          <Github className="w-5 h-5" />
                        </a>
                      )}
                      {project.links.demo && (
                        <a href={project.links.demo} target="_blank" rel="noreferrer" className="text-muted-foreground hover:text-primary transition-colors">
                          <ExternalLink className="w-5 h-5" />
                        </a>
                      )}
                    </div>
                  </div>
                  <CardTitle className="text-2xl font-bold group-hover:text-primary transition-colors">
                    {project.title}
                  </CardTitle>
                  <p className="text-sm text-secondary font-mono mt-1">{project.category}</p>
                </CardHeader>
                <CardContent className="flex-grow">
                  <p className="text-muted-foreground leading-relaxed mb-6">
                    {project.description}
                  </p>
                  <div className="flex flex-wrap gap-2 mt-auto">
                    {project.tech.map((t) => (
                      <Badge key={t} variant="secondary" className="font-mono text-xs bg-secondary/10 text-secondary hover:bg-secondary/20">
                        {t}
                      </Badge>
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
