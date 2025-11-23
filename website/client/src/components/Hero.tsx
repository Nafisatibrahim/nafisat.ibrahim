import { motion } from "framer-motion";
import { ArrowRight, Download } from "lucide-react";
import { Button } from "@/components/ui/button";
import heroBg from "@assets/generated_images/abstract_data_visualization_background.png";
import resumePdf from "@assets/NafisatIbrahim_Summer_2026_Internship_1763870597385.pdf";

export default function Hero() {
  return (
    <section id="hero" className="relative min-h-screen flex items-center justify-center overflow-hidden pt-16">
      {/* Background Image with Overlay */}
      <div className="absolute inset-0 z-0">
        <img 
          src={heroBg} 
          alt="Abstract Data Background" 
          className="w-full h-full object-cover opacity-40"
        />
        <div className="absolute inset-0 bg-gradient-to-b from-background/80 via-background/50 to-background" />
      </div>

      <div className="container mx-auto px-4 md:px-6 relative z-10">
        <div className="max-w-3xl">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
          >
            <h2 className="text-primary font-mono mb-4 tracking-wide">Hello, I'm</h2>
            <h1 className="text-5xl md:text-7xl font-bold tracking-tight mb-6 text-white">
              Nafisat Ibrahim
            </h1>
            <h2 className="text-2xl md:text-4xl font-light text-muted-foreground mb-8">
              Data Scientist & <span className="text-secondary">Quantitative Analyst</span>
            </h2>
            <p className="text-lg text-muted-foreground max-w-xl mb-10 leading-relaxed">
              Transforming complex datasets into actionable insights. Specializing in predictive modeling,
              automation, and business intelligence to drive decision-making.
            </p>
            
            <div className="flex flex-col sm:flex-row gap-4">
              <Button size="lg" className="text-base group" onClick={() => document.getElementById('projects')?.scrollIntoView({behavior: 'smooth'})}>
                View Projects
                <ArrowRight className="ml-2 w-4 h-4 group-hover:translate-x-1 transition-transform" />
              </Button>
              <Button size="lg" variant="outline" className="text-base gap-2" asChild>
                <a href={resumePdf} target="_blank" rel="noreferrer">
                  <Download className="w-4 h-4" />
                  Resume
                </a>
              </Button>
            </div>
          </motion.div>
        </div>
      </div>
      
      {/* Scroll Indicator */}
      <motion.div 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 1, duration: 1 }}
        className="absolute bottom-10 left-1/2 transform -translate-x-1/2 animate-bounce"
      >
        <div className="w-6 h-10 border-2 border-muted-foreground rounded-full flex justify-center p-1">
          <div className="w-1 h-2 bg-primary rounded-full" />
        </div>
      </motion.div>
    </section>
  );
}
