import Image from 'next/image'
import Link from 'next/link'

export default function Home() {
  return (
    <>
      <div className="sidebar">
        <Link href="/">Home</Link>
        <Link href="/">Rules</Link>
        <Link href="/items">Items</Link>
        <Link href="/">Lore</Link>
        <Link href="/">Your Characters</Link>
      </div>
      <div className="content">
        <title>Codex Homepage</title>
        <h2>Introduction</h2>
        <p>Cold Iron is a d20 system for a low-medium fantasy RPG, with fairly detailed combat and character progression through plot advancement and roleplay. It comes with its own setting, but the system should be easy enough to change to fit another one. Units are in the metric system.</p>
      </div>
    </>
  )
}
