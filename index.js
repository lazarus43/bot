const Discord = require("discord.js")
//const {Intents} =require("discord.js")
const {prefix, token} = require("./config.json")
const ytdl = require('ytdl-core');
const { MembershipScreeningFieldType } = require("discord-api-types");

const client = new Discord.Client({
    intents: [
        Discord.Intents.FLAGS.GUILDS,
        Discord.Intents.FLAGS.GUILD_MESSAGES,
        Discord.Intents.FLAGS.GUILD_VOICE_STATES,
        Discord.Intents.FLAGS.GUILD_MEMBERS,
        Discord.Intents.FLAGS.GUILD_MESSAGES_REACTION
    ]
});
client.once('ready', () => {
    console.log('Ready!');
});
client.once('reconnecting', () => {
    console.log('Reconnecting!');
});
client.once('disconnect', () => {
    console.log('Disconnect!');
});

client.login(token);
