using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TSI.BAE.Data
{
    public class TransducerSettings
    {
        public static string[] TransducerTypes = { "C3P2", "TDB1", "TBD2" };

        public TransducerSettings()
        {
            Type = TransducerTypes[0];
            ChannelID = 1;
            Name = "Channnel " + ChannelID.ToString();
        }

        public TransducerSettings(string name, int chan, string type)
        {
            Type = type;
            ChannelID = chan;
            Name = name;
        }

        public TransducerSettings(string type, int chan)
        {
            Type = type;
            ChannelID = chan;
            Name = "Channnel " + ChannelID.ToString();
        }
        public TransducerSettings(int chan)
        {
            Type = TransducerTypes[0];
            ChannelID = chan;
        }

        public string Name { get; set; }
        public bool Enabled { get; set; }
        public string Type { get; set; }
        public int ChannelID { get; set; }
    }
}
