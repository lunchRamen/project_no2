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
    genre: "로맨스",
    rating: 2,
    // burgerColor: "hsl(42, 70%, 50%)",
  },
  {
    genre: "액션",
    rating: 2,
    // burgerColor: "hsl(252, 100%, 100%)",
  },
  {
    genre: "공포",
    rating: 2,
    // burgerColor: "hsl(13, 100%, 100%)",
  },
  {
    genre: "스릴러",
    rating: 2,
    // burgerColor: "hsl(63, 100%, 100%)",
  },
  {
    genre: "빨리",
    rating: 2,
    // burgerColor: "hsl(87, 100%, 100%)",
  },
  {
    genre: "끝내줘",
    rating: 2,
    // burgerColor: "hsl(131, 100%, 100%)",
  },
  {
    genre: "제발",
    rating: 2,
    // burgerColor: "hsl(269, 100%, 100%)",
  },
];
const Chart = () => (
    <ResponsiveBar
      data={data}
      keys={["rating"]}
      indexBy="genre"
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
        legend: "genre",
        legendPosition: "middle",
        legendOffset: 32,
      }}
      axisLeft={{
        tickSize: 5,
        tickPadding: 5,
        tickRotation: 0,
        legend: "평점",
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
