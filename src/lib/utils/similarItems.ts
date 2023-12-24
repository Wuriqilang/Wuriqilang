// similar products
const similarItems = (currentItem: any, allItems: any[]) => {
  let categories: string[] = [];
  let tags: string[] = [];

  // set categories
  if (currentItem.data.categories.length > 0) {
    categories = currentItem.data.categories;
  }

  // set tags
  if (currentItem.data.tags.length > 0) {
    tags = currentItem.data.tags;
  }

  // filter by categories
  const filterByCategories = allItems.filter((item: any) =>
    categories.find((category) => item.data.categories.includes(category)),
  );

  // filter by tags
  const filterByTags = allItems.filter((item: any) =>
    tags.find((tag) => item.data.tags.includes(tag)),
  );

  // 查找两个arr的交集
  const intersection = filterByCategories.filter((item) => {
    return filterByTags.some((item2) => item.slug === item2.slug);
  });

  // merged after filter
  const mergedItems = [
    ...new Set([...intersection, ...filterByCategories, ...filterByTags]),
  ];

  // filter by slug
  const filterBySlug = mergedItems.filter(
    (product) => product.slug !== currentItem.slug,
  );

  // 如果超过3项，就截取前3项
  if (filterBySlug.length > 3) {
    return filterBySlug.slice(0, 3);
  }

  return filterBySlug;
};

export default similarItems;
