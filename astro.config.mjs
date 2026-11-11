// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

// Served from docs.flanker.wtf (a GitHub Pages custom domain = site root).
export default defineConfig({
  site: "https://docs.flanker.wtf",
  integrations: [
    starlight({
      title: "flanker",
      description:
        "Flanker setup guides and complete command reference.",
      customCss: ["./src/styles/brand.css"],
      components: { Header: "./src/components/DocsHeader.astro", ThemeProvider: "./src/components/DocsTheme.astro", ThemeSelect: "./src/components/Empty.astro" },
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
            { label: "Add to your profile", slug: "guides/user-install" },
            { label: "Typed slash commands", slug: "guides/slash-commands" },
            { label: "Find a command", slug: "commands" },
            { label: "Invite & setup", slug: "start/setup" },
          ],
        },
        {
          label: "Guides",
          items: [
            { label: "Security overview", slug: "guides/security" },
            { label: "Set up antinuke", slug: "guides/antinuke" },
            { label: "Set up antiraid", slug: "guides/antiraid" },
            { label: "Set up honeypot", slug: "guides/honeypot" },
            { label: "Moderation", slug: "guides/moderation" },
            { label: "Logging", slug: "guides/logging" },
            { label: "Welcome & messages", slug: "guides/welcome" },
            { label: "Tickets & applications", slug: "guides/tickets" },
            { label: "VoiceMaster", slug: "guides/voicemaster" },
            { label: "Valorant LFG", slug: "guides/lfg" },
            { label: "Minecraft bridge", slug: "guides/minecraft" },
            { label: "Music", slug: "guides/music" },
            { label: "Last.fm", slug: "guides/lastfm" },
            { label: "Friendships & gifts", slug: "guides/social" },
            { label: "Leveling", slug: "guides/leveling" },
            { label: "Live leaderboards", slug: "guides/live-leaderboards" },
            { label: "Embed and card builder", slug: "guides/embed-builder" },
            { label: "Bot profile and name style", slug: "guides/bot-profile" },
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
          collapsed: true,
          autogenerate: { directory: "commands" },
        },
      ],
    }),
  ],
});
