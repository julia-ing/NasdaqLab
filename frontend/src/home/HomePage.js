import Chart from './Chart';
import Prediction from './Prediction';
import Notification from './Notification';

function HomeTemplate() {
  return (
    <div className='home'>
      <div style={{ display: "flex" }}>
        <Chart></Chart>
        <Prediction></Prediction>
        <Notification></Notification>
      </div>
    </div>
  );
  // return (
  //   <Chart></Chart>
  // );
}

export default HomeTemplate;