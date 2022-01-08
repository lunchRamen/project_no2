/* eslint-disable prettier/prettier */
// install (please make sure versions match peerDependencies)
// yarn add @nivo/core @nivo/bar
import { ResponsiveBar } from "@nivo/bar";

// make sure parent container have a defined height when using
// responsive component, otherwise height will be 0 and
// no chart will be rendered.
// website examples showcase many properties,
// you'll often use just a few of them.
const data = [
  {
    country: "AD",
    burger: 35,
    // burgerColor: "hsl(42, 70%, 50%)",
  },
  {
    country: "AE",
    burger: 47,
    // burgerColor: "hsl(252, 100%, 100%)",
  },
  {
    country: "AF",
    burger: 22,
    // burgerColor: "hsl(13, 100%, 100%)",
  },
  {
    country: "AG",
    burger: 0,
    // burgerColor: "hsl(63, 100%, 100%)",
  },
  {
    country: "AI",
    burger: 125,
    // burgerColor: "hsl(87, 100%, 100%)",
  },
  {
    country: "AL",
    burger: 181,
    // burgerColor: "hsl(131, 100%, 100%)",
  },
  {
    country: "AM",
    burger: 4,
    // burgerColor: "hsl(269, 100%, 100%)",
  },
];
const Chart = () => (
    <ResponsiveBar
      data={data}
      keys={["burger"]}
      indexBy="country"
      margin={{ top: 50, right: 130, bottom: 50, left: 60 }}
      padding={0.3}
      valueScale={{ type: "linear" }}
      indexScale={{ type: "band", round: true }}
      // colors={{ datum: "white" }}
      axisTop={null}
      axisRight={null}
      axisBottom={{
        tickSize: 5,
        tickPadding: 5,
        tickRotation: 0,
        legend: "country",
        legendPosition: "middle",
        legendOffset: 32,
      }}
      axisLeft={{
        tickSize: 5,
        tickPadding: 5,
        tickRotation: 0,
        legend: "food",
        legendPosition: "middle",
        legendOffset: -40,
      }}
      theme={{
        background: "#222222",
        axis: {
          fontSize: "14px",
          tickColor: "#eee",
          ticks: {
            line: {
              stroke: "#555555"
            },
            text: {
              fill: "#ffffff"
            }
          },
          legend: {
            text: {
              fill: "#aaaaaa"
            }
          }
        },
        grid: {
          line: {
            stroke: "#555555"
          }
        }
      }}
      

      labelSkipWidth={12}
      labelSkipHeight={12}
      labelTextColor={{ from: "color", modifiers: [["darker", 1.6]] }}
      legends={[
        {
          dataFrom: "keys",
          anchor: "bottom-right",
          direction: "column",
          justify: false,
          translateX: 120,
          translateY: 0,
          itemsSpacing: 2,
          itemWidth: 100,
          itemHeight: 20,
          itemDirection: "left-to-right",
          itemOpacity: 0.85,
          symbolSize: 20,
          itemTextColor: "#ffffff",
          effects: [
            {
              on: "hover",
              style: {
                itemOpacity: 1,
              },
            },
          ],
        },
      ]}
      role="application"
      ariaLabel="Nivo bar chart demo"
      barAriaLabel={function (e) {
        return e.id + ": " + e.formattedValue + " in country: " + e.indexValue;
      }}
    />
);
export default Chart;
