import Chart from './Chart';
import Prediction from './Prediction';

function HomeTemplate() {
  return (
    <div className='home'>
      <div style={{ display: "flex" }}>
        <Chart></Chart>
        <Prediction></Prediction>
      </div>
    </div>
  );
  // return (
  //   <Chart></Chart>
  // );
}

export default HomeTemplate;