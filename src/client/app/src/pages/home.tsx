import { useUser } from "../context/UserContext";

const Home = () => {
  const { user } = useUser();
  
  return (
    <>
      <div className="text-3xl">{user?.username ? `@${user.username}` : user?.name}</div>
    </>
  );
}

export default Home;
