import Hero from "@/components/Hero";
import Systems from "@/components/Systems";
import HowIWork from "@/components/HowIWork";
import TechStack from "@/components/TechStack";
import Background from "@/components/Background";
import Contact from "@/components/Contact";

export default function Home() {
  return (
    <main className="max-w-5xl mx-auto px-6">
      <Hero />
      <Systems />
      <HowIWork />
      <TechStack />
      <Background />
      <Contact />
    </main>
  );
}
