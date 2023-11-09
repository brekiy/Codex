import Head from 'next/head';
import Layout from '../../components/layout';
import Link from 'next/link';

export default function ItemsTable() {
    // call db and load all items
    return (
        <Layout>
            <Head>
                <title>Items</title>
            </Head>
            <Link href="/">Back to home</Link>
        </Layout>
    );
}