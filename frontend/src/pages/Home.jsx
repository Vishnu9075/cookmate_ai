import Header from '../components/header';
import cookingBg from '../assets/cooking background.jpg';

function Home() {
  return (
    <div className="home-page relative">
      <Header />
      <div className="pt-5">

        <div
          className="bg-cover bg-center bg-no-repeat rounded-2xl overflow-hidden 
             w-[97%] h-[650px] mx-auto"
          style={{ backgroundImage: `url(${cookingBg})` }}
        >
          <h1 className="text-5xl font-bold text-white text-center absolute top-1/2 left-1/4 transform -translate-x-1/2 -translate-y-1/2 drop-shadow-lg">CookMate</h1>
        </div>
      </div>
    </div>
  );
}

export default Home;
