import { Link } from "wouter";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Separator } from "@/components/ui/separator";
import {
  Search,
  Sparkles,
  Filter,
  BarChart3,
  Bot,
  Shield,
  Smartphone,
  Database,
  ArrowDown,
  CheckCircle2,
  Circle,
  Clock,
  Github,
  Linkedin,
  GraduationCap,
  User,
} from "lucide-react";

const features = [
  {
    icon: Search,
    title: "Smart Scheme Discovery",
    description:
      "Browse central and state welfare programs with intelligent categorization and relevance scoring.",
  },
  {
    icon: Sparkles,
    title: "Personalized Recommendations",
    description:
      "Receive scheme suggestions tailored to your age group, sector interests, and eligibility profile.",
  },
  {
    icon: Filter,
    title: "Advanced Search & Filters",
    description:
      "Narrow results by ministry, income limit, sector, and location to find schemes that fit you.",
  },
  {
    icon: BarChart3,
    title: "Analytics Dashboard",
    description:
      "View scheme statistics, popularity trends, and sector-wise distribution at a glance.",
  },
  {
    icon: Bot,
    title: "AI-Powered Assistance",
    description:
      "Get guided help through an integrated assistant that answers questions about schemes and eligibility.",
  },
  {
    icon: Shield,
    title: "Secure User Accounts",
    description:
      "Session-based access with JWT authentication keeps your preferences and data protected.",
  },
  {
    icon: Smartphone,
    title: "Responsive Design",
    description:
      "A mobile-first interface that works seamlessly across phones, tablets, and desktops.",
  },
  {
    icon: Database,
    title: "Real-Time Data Access",
    description:
      "Live API connections ensure scheme information is always current and up to date.",
  },
];

const techStack = {
  frontend: ["React", "TypeScript", "Vite", "Tailwind CSS"],
  backend: ["Node.js", "Express.js"],
  database: ["MySQL"],
  authentication: ["JWT"],
  analytics: ["Linear Regression", "Recommendation Logic"],
  deployment: [
    "Docker compatible architecture",
    "Cloud deployment support",
  ],
};

const architectureSteps = [
  { label: "User", description: "Citizens access the portal via web browser" },
  { label: "Frontend", description: "React SPA with Vite and Tailwind CSS" },
  { label: "REST API", description: "Express.js endpoints for scheme data" },
  { label: "Database", description: "MySQL stores schemes, sectors, and metadata" },
  { label: "Analytics Layer", description: "Recommendation engine and predictive models" },
];

const roadmapPhases = [
  { phase: "Phase 1", status: "Completed", title: "Core Platform", done: true },
  { phase: "Phase 2", status: "Completed", title: "Authentication System", done: true },
  { phase: "Phase 3", status: "Completed", title: "Analytics Dashboard", done: true },
  { phase: "Phase 4", status: "In Progress", title: "Recommendation Engine", done: false, active: true },
  { phase: "Phase 5", status: "Planned", title: "Government API Integration", done: false },
  { phase: "Phase 6", status: "Planned", title: "Multilingual Support", done: false },
  { phase: "Phase 7", status: "Planned", title: "Mobile Application", done: false },
];

const securityItems = [
  "JWT Authentication",
  "Protected Routes",
  "Input Validation",
  "Secure API Access",
  "Environment Variable Protection",
];

function SectionHeading({
  title,
  subtitle,
}: {
  title: string;
  subtitle?: string;
}) {
  return (
    <div className="text-center max-w-2xl mx-auto mb-10 space-y-3">
      <h2 className="text-3xl font-bold tracking-tight">{title}</h2>
      {subtitle && (
        <p className="text-muted-foreground text-lg">{subtitle}</p>
      )}
    </div>
  );
}

export default function About() {
  return (
    <div className="flex flex-col">
      {/* Hero */}
      <section className="bg-muted/30 border-b py-20 px-4">
        <div className="container mx-auto max-w-3xl text-center space-y-6">
          <Badge variant="secondary" className="text-sm px-4 py-1">
            Civic Technology Platform
          </Badge>
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight">
            Yojna Connect
          </h1>
          <p className="text-xl text-muted-foreground leading-relaxed">
            An intelligent platform designed to simplify government scheme
            discovery through modern web technologies, analytics, and
            personalized recommendations.
          </p>
          <p className="text-base text-muted-foreground max-w-xl mx-auto">
            Our mission is to bridge the information gap between citizens and
            government welfare programs — making every eligible benefit
            discoverable, understandable, and accessible.
          </p>
          <div className="pt-4">
            <Link href="/schemes">
              <Button size="lg" className="text-base px-8">
                Explore Schemes
              </Button>
            </Link>
          </div>
        </div>
      </section>

      {/* Mission */}
      <section className="py-16 px-4">
        <div className="container mx-auto max-w-4xl">
          <SectionHeading
            title="Our Mission"
            subtitle="Making welfare information accessible to every citizen"
          />
          <div className="grid md:grid-cols-2 gap-6">
            {[
              "Simplifying access to welfare schemes across central and state governments",
              "Reducing information barriers that prevent citizens from claiming benefits",
              "Improving digital accessibility for users of all technical backgrounds",
              "Helping users find eligible schemes based on age, income, and sector",
              "Increasing awareness of government benefits through data-driven insights",
            ].map((item) => (
              <div key={item} className="flex gap-3 items-start">
                <CheckCircle2 className="h-5 w-5 text-primary shrink-0 mt-0.5" />
                <p className="text-muted-foreground">{item}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <Separator />

      {/* Features */}
      <section className="py-16 px-4 bg-muted/20">
        <div className="container mx-auto max-w-6xl">
          <SectionHeading
            title="Key Features"
            subtitle="Everything you need to discover and understand government schemes"
          />
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
            {features.map(({ icon: Icon, title, description }) => (
              <Card key={title} className="border shadow-sm">
                <CardHeader className="pb-3">
                  <div className="h-10 w-10 rounded-lg bg-primary/10 flex items-center justify-center mb-2">
                    <Icon className="h-5 w-5 text-primary" />
                  </div>
                  <CardTitle className="text-base">{title}</CardTitle>
                </CardHeader>
                <CardContent>
                  <CardDescription className="text-sm leading-relaxed">
                    {description}
                  </CardDescription>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Technology Stack */}
      <section className="py-16 px-4">
        <div className="container mx-auto max-w-4xl">
          <SectionHeading
            title="Technology Stack"
            subtitle="Built with modern, production-ready tools"
          />
          <div className="grid sm:grid-cols-2 gap-6">
            {Object.entries(techStack).map(([category, items]) => (
              <Card key={category}>
                <CardHeader className="pb-2">
                  <CardTitle className="text-sm uppercase tracking-wider text-muted-foreground font-medium">
                    {category.replace(/([A-Z])/g, " $1").trim()}
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <ul className="space-y-1.5">
                    {items.map((item) => (
                      <li key={item} className="text-sm font-medium">
                        {item}
                      </li>
                    ))}
                  </ul>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      <Separator />

      {/* Architecture */}
      <section className="py-16 px-4 bg-muted/20">
        <div className="container mx-auto max-w-lg">
          <SectionHeading
            title="System Architecture"
            subtitle="A straightforward, scalable request flow"
          />
          <div className="flex flex-col items-center gap-2">
            {architectureSteps.map((step, index) => (
              <div key={step.label} className="flex flex-col items-center w-full">
                <Card className="w-full text-center shadow-sm">
                  <CardHeader className="py-4">
                    <CardTitle className="text-lg">{step.label}</CardTitle>
                    <CardDescription>{step.description}</CardDescription>
                  </CardHeader>
                </Card>
                {index < architectureSteps.length - 1 && (
                  <ArrowDown className="h-5 w-5 text-muted-foreground my-1" />
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* AI & Analytics */}
      <section className="py-16 px-4">
        <div className="container mx-auto max-w-4xl">
          <SectionHeading
            title="AI & Analytics"
            subtitle="Data-driven insights that help citizens find the right schemes"
          />
          <div className="grid sm:grid-cols-2 gap-6">
            {[
              {
                title: "Recommendation Engine",
                body: "Analyzes user profiles and scheme attributes to surface the most relevant welfare programs for each visitor.",
              },
              {
                title: "Predictive Analytics",
                body: "Uses historical popularity and engagement data to forecast which schemes are most likely to benefit specific demographics.",
              },
              {
                title: "Linear Regression Models",
                body: "Statistical models identify patterns in eligibility criteria and user preferences to improve match accuracy over time.",
              },
              {
                title: "User Insights",
                body: "Aggregated, anonymized usage data helps identify coverage gaps and inform platform improvements.",
              },
              {
                title: "Future AI Expansion",
                body: "Planned integrations include natural language scheme search, document verification assistance, and multilingual chat support.",
              },
            ].map(({ title, body }) => (
              <Card key={title}>
                <CardHeader>
                  <CardTitle className="text-base">{title}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-sm text-muted-foreground leading-relaxed">
                    {body}
                  </p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      <Separator />

      {/* Security */}
      <section className="py-16 px-4 bg-muted/20">
        <div className="container mx-auto max-w-3xl">
          <SectionHeading
            title="Security"
            subtitle="Protecting user data at every layer"
          />
          <div className="flex flex-wrap justify-center gap-3">
            {securityItems.map((item) => (
              <Badge
                key={item}
                variant="outline"
                className="text-sm px-4 py-2"
              >
                <Shield className="h-3.5 w-3.5 mr-1.5" />
                {item}
              </Badge>
            ))}
          </div>
        </div>
      </section>

      {/* Roadmap */}
      <section className="py-16 px-4">
        <div className="container mx-auto max-w-4xl">
          <SectionHeading
            title="Roadmap"
            subtitle="Our journey from core platform to full-scale civic infrastructure"
          />
          <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {roadmapPhases.map(({ phase, status, title, done, active }) => (
              <Card
                key={phase}
                className={
                  active
                    ? "border-primary shadow-md"
                    : done
                      ? "border-green-200 dark:border-green-900"
                      : ""
                }
              >
                <CardHeader className="pb-2">
                  <div className="flex items-center justify-between">
                    <CardTitle className="text-sm text-muted-foreground font-medium">
                      {phase}
                    </CardTitle>
                    {done ? (
                      <CheckCircle2 className="h-4 w-4 text-green-600" />
                    ) : active ? (
                      <Clock className="h-4 w-4 text-primary" />
                    ) : (
                      <Circle className="h-4 w-4 text-muted-foreground" />
                    )}
                  </div>
                  <Badge
                    variant={done ? "secondary" : active ? "default" : "outline"}
                    className="w-fit text-xs"
                  >
                    {status}
                  </Badge>
                </CardHeader>
                <CardContent>
                  <p className="font-semibold">{title}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      <Separator />

      {/* Meet the Developer */}
      <section className="py-16 px-4 bg-muted/20">
        <div className="container mx-auto max-w-3xl">
          <SectionHeading
            title="Meet the Developer"
            subtitle="Built with passion for civic technology and accessible design"
          />
          <Card className="border shadow-sm overflow-hidden">
            <CardHeader className="pb-4">
              <div className="flex flex-col sm:flex-row sm:items-center gap-4">
                <div className="h-16 w-16 rounded-full bg-primary/10 flex items-center justify-center shrink-0">
                  <User className="h-8 w-8 text-primary" />
                </div>
                <div className="space-y-1">
                  <CardTitle className="text-2xl">Pawani Sharma</CardTitle>
                  <CardDescription className="text-base font-medium text-foreground/80">
                    Full-Stack Developer &amp; Civic Technology Enthusiast
                  </CardDescription>
                </div>
              </div>
            </CardHeader>
            <CardContent className="space-y-6">
              <p className="text-muted-foreground leading-relaxed">
                Pawani Sharma is a passionate developer focused on building
                accessible, user-friendly technology that solves real-world
                problems. Yojna Connect was developed as a modern civic
                technology platform that combines government scheme discovery
                with smart filtering and an interactive help assistant to create
                a simpler welfare access experience for every Indian citizen.
              </p>

              <div className="grid sm:grid-cols-2 gap-4">
                <div className="rounded-lg border bg-background p-4 space-y-1">
                  <div className="flex items-center gap-2 text-sm font-medium text-muted-foreground">
                    <GraduationCap className="h-4 w-4" />
                    Specialization
                  </div>
                  <p className="text-sm font-semibold leading-snug">
                    Full-Stack Web Development &amp; Civic Tech
                  </p>
                </div>
                <div className="rounded-lg border bg-background p-4 space-y-1">
                  <div className="text-sm font-medium text-muted-foreground">
                    Focus
                  </div>
                  <p className="text-sm font-semibold">
                    React &bull; Node.js &bull; Government Scheme Discovery
                  </p>
                </div>
              </div>

              <div className="flex flex-col sm:flex-row gap-3 pt-2">
                <a
                  href="https://github.com/pawani-2502"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex-1"
                >
                  <Button variant="outline" className="w-full gap-2">
                    <Github className="h-4 w-4" />
                    GitHub
                  </Button>
                </a>
                <a
                  href="https://github.com/pawani-2502"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex-1"
                >
                  <Button variant="outline" className="w-full gap-2">
                    <Linkedin className="h-4 w-4" />
                    LinkedIn
                  </Button>
                </a>
              </div>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* Final CTA */}
      <section className="py-20 px-4 bg-primary/5 border-t">
        <div className="container mx-auto max-w-2xl text-center space-y-6">
          <h2 className="text-3xl font-bold tracking-tight">
            Empowering Citizens Through Technology
          </h2>
          <p className="text-lg text-muted-foreground leading-relaxed">
            Yojna Connect bridges the gap between citizens and government
            welfare schemes using technology, analytics, and user-focused
            design.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center pt-2">
            <Link href="/schemes">
              <Button size="lg" className="w-full sm:w-auto px-8">
                Explore Schemes
              </Button>
            </Link>
            <Link href="/central-schemes">
              <Button
                size="lg"
                variant="outline"
                className="w-full sm:w-auto px-8"
              >
                Open Dashboard
              </Button>
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
}
