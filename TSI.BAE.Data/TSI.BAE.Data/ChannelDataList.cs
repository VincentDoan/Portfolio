using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TSI.BAE.Data
{
    /// <summary>
    /// A Class containg a List channels of ChannelData objects 
    /// </summary>

    public class ChannelDataList
    {
        List<ChannelData> channels = new List<ChannelData>(TestConfig.ChannelCount);

        public List<ChannelData> Channels
        {
            get { return channels; }
            set { channels = value; }
        }

        public ChannelDataList()
        { 

        }

        public ChannelDataList(int newSize)
        {
            TestConfig.ChannelCount = newSize;
        }
    }

}
