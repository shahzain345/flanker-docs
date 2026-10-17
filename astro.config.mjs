// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

// Served from docs.flanker.wtf (a GitHub Pages custom domain = site root).
export default defineConfig({
  site: "https://docs.flanker.wtf",
  integrations: [
    starlight({
      title: "flanker docs",
      description:
        "Documentation for flanker, the all-in-one Discord security, moderation and management bot.",
      customCss: ["./src/styles/brand.css"],
      social: {
        discord: "https://discord.gg/yRyTAHmvxJ",
      },
      editLink: {
        baseUrl: "https://github.com/shahzain345/flanker-docs/edit/main/",
      },
      sidebar: [
        {
          label: "Start here",
          items: [
            { label: "Getting started", slug: "start/getting-started" },
            { label: "Invite & setup", slug: "start/setup" },
          ],
        },
        {
          label: "Guides",
          items: [
            { label: "Security", slug: "guides/security" },
            { label: "Moderation", slug: "guides/moderation" },
            { label: "Logging", slug: "guides/logging" },
            { label: "Welcome & messages", slug: "guides/welcome" },
            { label: "Tickets & applications", slug: "guides/tickets" },
            { label: "VoiceMaster", slug: "guides/voicemaster" },
            { label: "Leveling", slug: "guides/leveling" },
            { label: "Reaction roles & starboard", slug: "guides/reaction-roles" },
            { label: "Social notifications", slug: "guides/notifications" },
            { label: "Invite tracking", slug: "guides/invites" },
            { label: "Birthdays", slug: "guides/birthdays" },
            { label: "The dashboard", slug: "guides/dashboard" },
          ],
        },
        {
          label: "Resources",
          items: [
            { label: "Embed & card scripting", slug: "resources/scripting" },
            { label: "Variables", slug: "resources/variables" },
          ],
        },
        {
          label: "Command reference",
          autogenerate: { directory: "commands" },
        },
      ],
    }),
  ],
});
