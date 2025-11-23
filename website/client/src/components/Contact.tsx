import { motion } from "framer-motion";
import { Mail, Linkedin, Github, MapPin } from "lucide-react";
import { Button } from "@/components/ui/button";

export default function Contact() {
  return (
    <section id="contact" className="py-24 bg-background relative overflow-hidden">
        {/* Subtle Grid Background */}
        <div className="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px]" />
      
      <div className="container mx-auto px-4 md:px-6 relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="max-w-2xl mx-auto text-center"
        >
          <p className="text-primary font-mono mb-4">05. What's Next?</p>
          <h2 className="text-4xl md:text-5xl font-bold mb-6">Get In Touch</h2>
          <p className="text-muted-foreground text-lg mb-10 leading-relaxed">
            I'm currently looking for new opportunities in Data Science and Analytics. 
            Whether you have a question or just want to say hi, I'll try my best to get back to you!
          </p>

          <div className="flex flex-col sm:flex-row gap-4 justify-center mb-12">
            <Button size="lg" className="h-12 px-8 text-base" asChild>
              <a href="mailto:nafisat.larissa.ibrahim@gmail.com">
                <Mail className="mr-2 w-5 h-5" />
                Say Hello
              </a>
            </Button>
            <Button size="lg" variant="outline" className="h-12 px-8 text-base" asChild>
              <a href="https://www.linkedin.com/in/nafisatibrahim/" target="_blank" rel="noreferrer">
                <Linkedin className="mr-2 w-5 h-5" />
                LinkedIn
              </a>
            </Button>
          </div>

          <div className="pt-10 border-t border-border/50 flex flex-col md:flex-row justify-between items-center gap-4 text-sm text-muted-foreground font-mono">
            <div className="flex items-center gap-2">
               <MapPin className="w-4 h-4" /> Waterloo, ON
            </div>
            <div className="flex gap-6">
                <a href="https://github.com/Nafisatibrahim" target="_blank" rel="noreferrer" className="hover:text-primary transition-colors">
                    <Github className="w-5 h-5" />
                </a>
                <a href="https://www.linkedin.com/in/nafisatibrahim/" target="_blank" rel="noreferrer" className="hover:text-primary transition-colors">
                    <Linkedin className="w-5 h-5" />
                </a>
            </div>
            <p>© {new Date().getFullYear()} Nafisat Ibrahim</p>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
